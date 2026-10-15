def predict_label(value):
    """A tiny example function for CI testing."""
    return "positive" if value >= 0.5 else "negative"

def get_message():
    """Return a short message describing the demo app."""
    return "Git and CI/CD demo for MLOps"

if __name__ == "__main__":
    print(get_message())
    print("Prediction:", predict_label(0.8))
