import json, pytest
import datetime
from flask import Flask,render_template,request,redirect,flash,url_for


def loadClubs():
    with open('clubs.json') as c:
         listOfClubs = json.load(c)['clubs']
         return listOfClubs


def loadCompetitions():
    with open('competitions.json') as comps:
         listOfCompetitions = json.load(comps)['competitions']
         return listOfCompetitions


app = Flask(__name__)
app.secret_key = 'something_special'

competitions = loadCompetitions()
clubs = loadClubs()
club_points_by_competitons = {}

@app.route('/')
def index():
    return render_template('index.html')


@app.route('/showSummary',methods=['POST'])
def showSummary():
    club = next((club for club in clubs if club['email'] == request.form['email']), None)
    if club == None:
        flash('Email not found.')
        return redirect(url_for('index'), code=301)
    elif 'email' in club:
        return render_template('welcome.html',club=club,competitions=competitions)

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
    competition = next((c for c in competitions if c['name'] == request.form['competition']), None)
    club = next((club for club in clubs if club['name'] == request.form['club']), None)
    placesRequired = int(request.form['places'])


    points_club = int(club['points'])

    if competition['name'] not in club_points_by_competitons:
        club_points_by_competitons[competition['name']] = {}

    if club['name'] not in club_points_by_competitons[competition['name']]:
        club_points_by_competitons[competition['name']][club['name']] = 0
    
    club_points_by_competitons_before_purchase = club_points_by_competitons[competition['name']][club['name']]
    club_points_by_competitons[competition['name']][club['name']] += placesRequired
    club_points_by_competitons_after_purchase = club_points_by_competitons[competition['name']][club['name']]

    date_competition = datetime.datetime.strptime(competition['date'], '%Y-%m-%d %H:%M:%S')
    date_now = datetime.datetime.now()
    if club_points_by_competitons_after_purchase <= 12 and placesRequired <= 12 and points_club >= placesRequired and date_competition > date_now:   
            competition['numberOfPlaces']   = int(competition['numberOfPlaces'])-placesRequired
            club_points_by_competitons[competition['name']][club['name']] = club_points_by_competitons_after_purchase
            club['points'] = int(club['points'])-placesRequired
            flash('Points general updated')
            flash('Date competition valid')
            flash('Great-booking complete!')
    elif(date_competition < date_now): 
        club_points_by_competitons[competition['name']][club['name']] = club_points_by_competitons_before_purchase
        flash('Date competition expired')
    elif points_club < placesRequired:
            print(points_club)
            print(placesRequired)
            flash('Not enought points')
            club_points_by_competitons[competition['name']][club['name']] = club_points_by_competitons_before_purchase    
    elif club_points_by_competitons_after_purchase > 12 :
            # Remet dans l'état initial si test pas concluant
            flash('Max points is 12 for a club in a competition')
            club_points_by_competitons[competition['name']][club['name']] = club_points_by_competitons_before_purchase
    else:
        print('arthur')
        flash('Max points is 12 for a club in a competition')
        club_points_by_competitons[competition['name']][club['name']] = club_points_by_competitons_before_purchase

    return render_template('welcome.html', club=club, competitions=competitions)


# TODO: Add route for points display


@app.route('/logout')
def logout():
    competitions = loadCompetitions()
    clubs = loadClubs()
    club_points_by_competitons = {}
    return redirect(url_for('index'))