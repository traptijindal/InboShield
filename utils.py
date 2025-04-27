import numpy as np

def get_label_and_meter(spam_confidence, ham_confidence):
    diff = abs(spam_confidence - ham_confidence)

    if spam_confidence > ham_confidence:
        if diff > 60:
            label = "Confidently Spam ❌❌"
        elif diff > 30:
            label = "Possibly Spam ⚠️"
        else:
            label = "Uncertain 🤔"
    else:
        if diff > 60:
            label = "Confidently Ham ✅✅"
        elif diff > 30:
            label = "Likely Ham 🙂"
        else:
            label = "Uncertain 🤔"

    bars = int(ham_confidence // 20)
    meter = "🟢" * bars + "⚫️" * (5 - bars)

    return label, meter
