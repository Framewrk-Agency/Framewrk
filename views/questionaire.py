@app.route('/question', methods=['GET', 'POST'])
def question():
    """Entry point for quetions."""
    return render_template('/question.html', template='qotd-template')


@app.route('/interact', methods=['GET', 'POST'])
def onboardingtype():
    """Business-type onboarding."""
    return render_template('/onboarding.html', category='business', questiontext='What type of business do you have?')
