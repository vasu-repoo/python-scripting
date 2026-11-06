
import pygame
import random

pygame.init()

WIDTH, HEIGHT = 600, 700
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Space Shooter")

clock = pygame.time.Clock()
font = pygame.font.SysFont(None, 36)

player = pygame.Rect(275, 600, 50, 50)
bullets = []
enemies = []

score = 0
health = 3
running = True

SPAWN = pygame.USEREVENT + 1
pygame.time.set_timer(SPAWN, 900)

while running:
    clock.tick(60)
    screen.fill((10, 10, 35))

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

        if event.type == SPAWN:
            enemies.append(pygame.Rect(
                random.randint(0, WIDTH - 40), 0, 40, 40
            ))

        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_SPACE:
                bullets.append(
                    pygame.Rect(player.centerx - 4, player.top, 8, 15)
                )

    keys = pygame.key.get_pressed()

    if keys[pygame.K_LEFT] and player.left > 0:
        player.x -= 6
    if keys[pygame.K_RIGHT] and player.right < WIDTH:
        player.x += 6

    # Move bullets
    for bullet in bullets[:]:
        bullet.y -= 9
        if bullet.bottom < 0:
            bullets.remove(bullet)

    # Move enemies
    for enemy in enemies[:]:
        enemy.y += 4

        if enemy.top > HEIGHT:
            enemies.remove(enemy)
            health -= 1
            continue

        if enemy.colliderect(player):
            enemies.remove(enemy)
            health -= 1

    # Bullet collisions
    for bullet in bullets[:]:
        for enemy in enemies[:]:
            if bullet.colliderect(enemy):
                bullets.remove(bullet)
                enemies.remove(enemy)
                score += 10
                break

    # Draw player
    pygame.draw.rect(screen, (0, 200, 255), player)

    # Draw bullets
    for bullet in bullets:
        pygame.draw.rect(screen, (255, 255, 0), bullet)

    # Draw enemies
    for enemy in enemies:
        pygame.draw.rect(screen, (255, 50, 70), enemy)

    # Display score and health
    screen.blit(font.render(f"Score: {score}", True, (255, 255, 255)), (10, 10))
    screen.blit(font.render(f"Health: {health}", True, (255, 255, 255)), (440, 10))

    if health <= 0:
        screen.fill((15, 15, 40))
        msg = font.render("GAME OVER!", True, (255, 50, 50))
        final = font.render(f"Final Score: {score}", True, (255, 255, 255))
        screen.blit(msg, (220, 300))
        screen.blit(final, (210, 350))
        pygame.display.flip()
        pygame.time.wait(2500)
        running = False
        continue

    pygame.display.flip()

pygame.quit()