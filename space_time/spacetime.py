import pygame
import math

pygame.init()

WIDTH, HEIGHT = 1000, 800
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Časopriestor a plynutie času")

BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
YELLOW = (255, 255, 0)
BLUE = (0, 0, 255)
GRAY = (200, 200, 200)

center_x, center_y = WIDTH // 2, HEIGHT // 2
star_radius = 40
planets = [
    {"radius": 12, "distance": 150, "angle": 0, "speed": 0.02},
    {"radius": 10, "distance": 250, "angle": 0, "speed": 0.01},
    {"radius": 8, "distance": 350, "angle": 0, "speed": 0.007},
]

clock = pygame.time.Clock()
running = True

def project_3D(x, y, z):
    """Jednoduchá perspektívna projekcia 3D na 2D"""
    scale = 1 / (1 + z/500)
    proj_x = int(center_x + (x - center_x) * scale)
    proj_y = int(center_y + (y - center_y) * scale)
    return proj_x, proj_y

def draw_star():
    pygame.draw.circle(screen, YELLOW, (center_x, center_y), star_radius)

def draw_clock(x, y, time_factor):
    """Nakreslí mini hodiny ukazujúce plynutie času"""
    # Čím tmavšie, tým pomalšie
    clock_radius = 8
    pygame.draw.circle(screen, GRAY, (int(x), int(y)), clock_radius, 1)
    angle = math.radians(pygame.time.get_ticks() * 0.05 * time_factor)
    hand_length = 6
    hand_x = x + hand_length * math.cos(angle)
    hand_y = y + hand_length * math.sin(angle)
    pygame.draw.line(screen, GRAY, (x, y), (hand_x, hand_y), 2)

while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    screen.fill(BLACK)
    draw_star()

    for planet in planets:
        # simulácia ohybu priestoru a času
        angle = planet["angle"]
        distance = planet["distance"] * (1 - 0.3 * math.exp(-planet["distance"]/200))
        z = -50 * math.exp(-planet["distance"]/200)  # simulácia 3D hĺbky
        x = center_x + distance * math.cos(angle)
        y = center_y + distance * math.sin(angle)
        proj_x, proj_y = project_3D(x, y, z)

        # simulácia spomalenia času
        time_factor = 1 - 0.7 * math.exp(-planet["distance"]/200)
        color = (int(0+255*(1-time_factor)), int(0+255*time_factor), 255)
        radius = max(1, int(planet["radius"] * time_factor))
        pygame.draw.circle(screen, color, (proj_x, proj_y), radius)

        # ukazovateľ času vedľa planéty
        draw_clock(proj_x + radius + 5, proj_y, time_factor)

        # pohyb planéty spomalený gravitačným časom
        planet["angle"] += planet["speed"] * time_factor

    # vizualizácia ohybu priestoru ako kruhy
    for r in range(60, 400, 30):
        pygame.draw.circle(screen, WHITE, (center_x, center_y), int(r * (1 - 0.2 * math.exp(-r/200))), 1)

    pygame.display.flip()
    clock.tick(60)

pygame.quit()