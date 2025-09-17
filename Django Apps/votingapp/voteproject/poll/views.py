from django.shortcuts import render, redirect

def poll_view(request):
    if 'candidates' not in request.session:
        request.session['candidates'] = []
        request.session['votes'] = [0, 0]
        request.session['reveal'] = False

    candidates = request.session['candidates']
    votes = request.session['votes']
    reveal = request.session.get('reveal', False)

    # Step 1: Enter candidate names
    if request.method == 'POST' and 'set_candidates' in request.POST:
        name1 = request.POST.get('name1', '').strip()
        name2 = request.POST.get('name2', '').strip()
        if name1 and name2:
            request.session['candidates'] = [name1, name2]
            request.session['votes'] = [0, 0]
            request.session['reveal'] = False
            return redirect('poll_home')

    # Step 2: Vote
    if request.method == 'POST' and 'vote_for' in request.POST:
        idx = int(request.POST.get('vote_for'))
        votes[idx] += 1
        request.session['votes'] = votes
        return redirect('poll_home')

    # Step 3: Reveal results
    if request.method == 'POST' and 'reveal' in request.POST:
        request.session['reveal'] = True
        return redirect('poll_home')

    # Reset system for new poll
    if request.method == 'POST' and 'reset' in request.POST:
        request.session.flush()
        return redirect('poll_home')

    candidates = request.session['candidates']
    votes = request.session['votes']
    reveal = request.session['reveal']

    context = {
        'candidates': candidates,
        'votes': votes,
        'reveal': reveal,
    }
    return render(request, 'poll/home.html', context)
