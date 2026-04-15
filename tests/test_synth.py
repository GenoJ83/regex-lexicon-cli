from src.generator.synth import generate_matching_email

def test_synth_email():
    e = generate_matching_email()
    assert "@" in e and e.endswith(".com")
