"""
Control the sound
"""
import pygame


def volume_percent(_num: int = 50) -> float:
    """Change volume in percent

    Args:
        _num (int, optional): Percent change of volume. Defaults to 50.

    Returns:
        float: Result of change
    """
    _volume = pygame.mixer.music.get_volume()
    _volume = _volume * _num/100

    return _volume

# Initialization
pygame.init()
pygame.mixer.init()
soundtrack = pygame.mixer.music
pygame.mixer.pre_init(frequency=44100, size=-16, channels=2, buffer=512)

# Soundtrack
soundtrack.load(r"assets\sound\Action_Rhythms.mp3")
soundtrack.play()

soundtrack.set_volume(volume_percent(20))

flap_sound = pygame.mixer.Sound(r'assets\sound\sfx_wing.wav')
flap_sound.set_volume(volume_percent(20))
hit_sound = pygame.mixer.Sound(r'assets\sound\sfx_hit.wav')
hit_sound.set_volume(volume_percent(20))
score_sound = pygame.mixer.Sound(r'assets\sound\sfx_point.wav')
score_sound.set_volume(volume_percent(10))
SCORE_SOUND_COUND_DOWN = 50.
