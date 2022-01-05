import json
from flask import Flask,render_template,request,redirect,flash,url_for, session


def loadClubs():
    with open('clubs.json') as c:
         listOfClubs = json.load(c)['clubs']
         return listOfClubs


def loadCompetitions():
    with open('competitions.json') as comps:
         listOfCompetitions = json.load(comps)['competitions']
         return listOfCompetitions

def create_app(config):
    app = Flask(__name__)
    app.secret_key = 'something_special'

    competitions = loadCompetitions()
    clubs = loadClubs()

    @app.route('/')
    def index():
        return render_template('index.html')

    @app.route('/showSummary',methods=['POST'])
    def showSummary():
        try:
            club = [club for club in clubs if club['email'] == request.form['email']][0]
            return render_template('welcome.html',club=club,competitions=competitions)
        except IndexError:
            flash("Sorry, that email was not found.", 'error')
            return render_template('index.html') , 405


    @app.route('/book/<competition>/<club>')
    def book(competition,club):
        foundClub = [c for c in clubs if c['name'] == club][0]
        foundCompetition = [c for c in competitions if c['name'] == competition][0]
        if foundClub and foundCompetition:
            return render_template('booking.html',club=foundClub,competition=foundCompetition)
        else:
            flash("Something went wrong-please try again")
            return render_template('welcome.html', club=club, competitions=competitions)


    @app.route('/purchasePlaces',methods=['POST'])
    def purchasePlaces():
        
        # Verify previous actions to avoid favoritism (book more than 12 per competitions bu one club).
        if 'track' not in session:
            keys = [x['name'] for x in competitions]
            track = {x: [] for x in keys}
            session['track'] = track
        memory = session.get('track')
        competition = [c for c in competitions if c['name'] == request.form['competition']][0]
        club = [c for c in clubs if c['name'] == request.form['club']][0]
        placesRequired = int(request.form['places'])
        points_club = int(club['points'])

        to_check = memory[competition['name']]
        already_booked_number = to_check.count(club['name'])
        number_place_available = int(competition['numberOfPlaces'])
        if placesRequired > number_place_available:
            flash(
                f'You can not book more than {number_place_available} for this tournament.')
        elif placesRequired <= points_club and 0 < placesRequired <= 12 and (already_booked_number + placesRequired) <= 12:
            competition['numberOfPlaces'] = int(competition['numberOfPlaces']) - placesRequired
            club['points'] = points_club - placesRequired
            
            # Add track of reservation to session to avoid favoritism (book more than 12 per competitions bu one club).
            memory[competition['name']].extend([club['name']] * placesRequired)
            session['track'] = memory
            flash('Great-booking complete!')
        elif 0 < placesRequired > points_club:
            flash('Your club do not have enough points to do this.', 'error')
        else:
            flash('You can not book more than (12) places per competition and less than (1) if you choose to participate.', 'error')

        return render_template('welcome.html', club=club, competitions=competitions)

    # TODO: Add route for points display


    @app.route('/logout')
    def logout():
        session.pop('track', None)
        return redirect(url_for('index'))
    
    return app