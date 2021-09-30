from flask import render_template, request, redirect, url_for,abort,flash
from . import main
from flask_login import login_required,current_user
from ..models import User,Song,Review
from .forms import UpdateProfile,SongForm,ReviewForm
from .. import db, photos


@main.route('/')
def index():
    """
    Index view function that returns the index html page. Which is the homepage.
    """
    all_songs = Song.query.order_by('id').all()
    print(all_songs)
    main_title = 'First Impression songs'
    return render_template('index.html', main_title=main_title,all_songs=all_songs)

@main.route('/user/<uname>')
def profile(uname):
    user = User.query.filter_by(username=uname).first()

    if user is None:
        abort(404)

    return render_template("profile/profile.html", user=user)


@main.route('/user/<uname>/update', methods=['GET', 'POST'])
@login_required
def update_profile(uname):
    user = User.query.filter_by(username=uname).first()
    if user is None:
        abort(404)

    form = UpdateProfile()

    if form.validate_on_submit():
        user.bio = form.bio.data

        db.session.add(user)
        db.session.commit()

        return redirect(url_for('.profile', uname=user.username))

    return render_template('profile/update.html', form=form)


@main.route('/user/<uname>/update/pic', methods=['POST'])
@login_required
def update_pic(uname):
    user = User.query.filter_by(username=uname).first()
    if 'photo' in request.files:
        filename = photos.save(request.files['photo'])
        path = f'photos/{filename}'
        user.profile_pic_path = path
        db.session.commit()
    return redirect(url_for('main.profile', uname=uname))



@main.route('/music/review/new/<int:id>', methods = ['GET','POST'])
def new_review(id):
    form = ReviewForm()
    song =Song.get_songs(id)

    if form.validate_on_submit():
        title = form.title.data
        review = form.review.data
        new_review = Review(song.id,title,review)
        new_review.save_review()
        return redirect(url_for('song',id = song.id ))

    title = f'{song.title} review'
    return render_template('new_review.html',title = title, review_form=form,)


@main.route('/song/new', methods = ['GET','POST'])
@login_required
def new_song():
    form = SongForm()
    if form.validate_on_submit():
        title = form.title.data
        category = form.category.data
        artist=form.artist.data
        # user_song = form.song_url.data
        new_song = Song(title=title, category=category, artist=artist, user=current_user)
        #save song
        new_song.save_song()
        return redirect(url_for('.index',id=new_song.id))
    page_title = "Add new Song"
    return render_template('new_song.html', song_form = form,page_title= page_title)


@main.route('/category/Gospel', methods=['GET'])
def Gospel():
    """
    Function for displaying Gospel songs page.
    """
    songs = Song.get_songs('gospel')
    gospel_title = "gospel songs"
    return render_template('songs/gospel.html', gospel_title = gospel_title, gospel_songs = songs)

@main.route('/category/Reggae', methods=['GET'])
def Reggae():
    """
    Function for displaying reggae songs page.
    """
    songs = Song.get_songs('reggae')
    reggae_title = "This page will display reggae songs"
    return render_template('songs/reggae.html', reggae_title = reggae_title, reggae_songs = songs)

@main.route('/category/HipHop', methods=['GET'])
def HipHop():
    """
    Function for displaying HipHop songs page.
    """
    songs = Song.get_songs('hiphop')
    hiphop_title = "This page will display hiphop songs"
    return render_template('songs/hiphop.html', hiphop_title =hiphop_title, hiphop_songs = songs)

@main.route('/category/R&B', methods=['GET'])
def RnB():
    """
    Function for displaying RnB songs page.
    """
    songs = Song.get_songs('RnB')
    RnB_title = "This page will display RnB songs"
    return render_template('songs/RnB.html', RnB_title = RnB_title, RnB_songs = songs)

