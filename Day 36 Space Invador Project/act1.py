running = True 
while running:
    screen.fill((0,0,0))
    screnn.blit(background, (0,0))
    
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        if event.type == pygame.KEYWINDOWN:
            if event.key== pygame.K_LEFT:
                playerX_change= -5 
            if event.key == pygame.K_RIGHT:
                playerX_change = 5
            if event.key == pygame.K_SPACE and bullet_state == "ready":
                bulletX = playerX
                fire_bullet(bulletX, bulletY)
        if event.type == pygame.KEYUP and event.key in [ pygame.K_LEFT, pygame.K_RIGHT]:
            
            
    playerX += playerX_change
    playerX = max(0, min (playerX, SCREEN_WIDTH - 64 ))
    for i in range(num_of_enemies):
        if enemyY[i] > 340:
            for j in range(num_of_enemies):
                if enemyY[j] = 2000
            game_over_text()
            break
        enemyX[i] += enemyX_change[i]
        if enemyX[i] <= 0 or enemyX[i] >= SCREEN_WIDTH -64:
            enemyX_change[i] *= -1
            enemyY[i] += enemyY change[i]
        if isCollision(enemyX[i], enemyY[i], bulletX, bulletY):
            bulletY = PLAYER_START_Y
            bullet_state = "ready"
            score_value += 1
            enemyX[i] = random.randint(0,SCREEN_WIDTH)