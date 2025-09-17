import random
from django.shortcuts import render

EMOJI_MAP = {
    "rock": "🪨",
    "paper": "📄",
    "scissors": "✂️"
}
CHOICES = ["rock", "paper", "scissors"]

def rps_view(request):
    # Reset session if reset button clicked
    if request.method == "POST" and request.POST.get("reset"):
        request.session.flush()

    user_score = request.session.get("user_score", 0)
    computer_score = request.session.get("computer_score", 0)
    user_choice = None
    computer_choice = None
    result = None

    if request.method == "POST" and not request.POST.get("reset"):
        user_choice = request.POST.get("choice")
        computer_choice = random.choice(CHOICES)

        if user_choice == computer_choice:
            result = "Tie!"
        elif (
            (user_choice == "rock" and computer_choice == "scissors") or
            (user_choice == "paper" and computer_choice == "rock") or
            (user_choice == "scissors" and computer_choice == "paper")
        ):
            result = "You win!"
            user_score += 1
        else:
            result = "Computer wins!"
            computer_score += 1

        request.session["user_score"] = user_score
        request.session["computer_score"] = computer_score

    emoji_choices = [(move, EMOJI_MAP[move]) for move in CHOICES]

    context = {
        "emoji_choices": emoji_choices,
        "user_choice": user_choice,
        "computer_choice": computer_choice,
        "result": result,
        "user_score": user_score,
        "computer_score": computer_score,
    }
    return render(request, "rps/home.html", context)
