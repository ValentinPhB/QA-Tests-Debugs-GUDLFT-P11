import json
from datetime import datetime

from flask import Flask, render_template, request, redirect, flash, url_for, session


def loadClubs():
    with open('clubs.json') as c:
        return json.load(c)['clubs']


def loadCompetitions():
    with open('competitions.json') as comps:
        return json.load(comps)['competitions']

# Determine how many points needed for book one place 
def ratio():
    return 3

def create_app(config):
    app = Flask(__name__)
    app.secret_key = 'something_special'

    competitions = loadCompetitions()
    clubs = loadClubs()
    
    # Checking actual date (to pass to template welcome.html)
    date_now = datetime.now().strftime("%Y-%m-%d %H:%M:%S")

    # points_for_places : how many points for book one place. Default = 1
    points_for_places = ratio()
    
    @app.route('/')
    def index():
        return render_template('index.html')

    @app.route('/showSummary', methods=['POST'])
    def showSummary():
        existing_email = [c['email'] for c in clubs]
        if request.form['email'] in existing_email:
            club = [club for club in clubs if club['email']
                    == request.form['email']][0]
            return render_template('welcome.html', club=club, clubs=clubs, competitions=competitions, date_now=date_now, points_for_places=points_for_places)
        flash("Sorry, that email was not found.", 'error')
        return render_template('index.html'), 405

    @app.route('/book/<competition>/<club>')
    def book(competition, club):
        existing_club = [c['name'] for c in clubs]
        existing_competition = [comp['name'] for comp in competitions]
        if competition in existing_competition and club in existing_club:
            foundClub = [c for c in clubs if c['name'] == club][0]
            foundCompetition = [
                c for c in competitions if c['name'] == competition][0]
            return render_template('booking.html', club=foundClub, competition=foundCompetition, points_for_places=points_for_places)
        flash("Something went wrong-please try again")
        return render_template('welcome.html', club=club, clubs=clubs, competitions=competitions, date_now=date_now, points_for_places=points_for_places)

    @app.route('/purchasePlaces', methods=['POST'])
    def purchasePlaces():
        # Use or create dict in session to keep trace and avoid favoritism (<= 12 places by club per competitions).
        if 'track' not in session:
            keys = [x['name'] for x in competitions]
            track = {x: [] for x in keys}
            session['track'] = track
        memory = session.get('track')

        # Extract specified club and competition
        competition = [c for c in competitions if c['name']
                       == request.form['competition']][0]
        club = [c for c in clubs if c['name'] == request.form['club']][0]

        # Get information
        placesRequired = int(request.form['places'])
        points_club = int(club['points'])

        # Checking if club has already booked some places and how many.
        to_check = memory[competition['name']]
        already_booked_number = to_check.count(club['name'])
        number_place_available = int(competition['numberOfPlaces'])

        # Date for checking
        date_competition = competition['date']
        
        # Answer if post request to passed competition
        if date_competition < date_now:
            flash('You can not book places for a past competition.')
            
        # Places available
        elif placesRequired > number_place_available:
            flash(
                f'You can not book {placesRequired} places for this competition. Only {number_place_available} places left.')

        # <= 12 places booked
        elif placesRequired * points_for_places <= points_club and 0 < placesRequired <= 12 and (already_booked_number + placesRequired) <= 12:
            competition['numberOfPlaces'] = int(
                competition['numberOfPlaces']) - placesRequired
            club['points'] = points_club - placesRequired * points_for_places

            # Add track of reservation to session to avoid favoritism (book more than 12 per competitions bu one club).
            memory[competition['name']].extend([club['name']] * placesRequired)
            session['track'] = memory
            flash(
                f'Great-booking complete! You have book {placesRequired} places.')

        # Enough points to book ?
        elif 0 < placesRequired * points_for_places and placesRequired * points_for_places > points_club:
            flash(
                f'Your club do not have enough points to do this. You need {points_for_places} point(s) for ONE place.', 'error')

        # More than 12 places booked for on copetition
        else:
            flash('You can not book more than (12) places per competition and less than (1) if you choose to participate.', 'error')

        return render_template('welcome.html', club=club, clubs=clubs, competitions=competitions, date_now=date_now, points_for_places=points_for_places)

    @app.route('/table', methods=['GET'])
    def table():
        return render_template('table.html', clubs=clubs)

    @app.route('/logout')
    def logout():
        session.pop('track', None)
        return redirect(url_for('index'))

    return app
