class PongProgram:
    GAME_WIDTH = 900
    GAME_HEIGHT = 500

    def __init__(self):
        self.player_score = 0
        self.computer_score = 0
        self.window = None
        self.canvas = None

        self.left_paddle_x = 50
        self.left_paddle_y = 150
        self.left_paddle_width = 50
        self.left_paddle_height = 200
        self.left_paddle_movement = 0
        self.left_paddle = None

        self.right_paddle_x = 800
        self.right_paddle_y = 150
        self.right_paddle_width = 50
        self.right_paddle_height = 200
        self.right_paddle_movement = 0
        self.right_paddle = None

        self.ball_x = 435
        self.ball_y = 235
        self.ball_width = 30
        self.ball_height = 30
        self.ball_movement_x = 1
        self.ball_movement_y = 1
        self.ball_speed = 1
        self.ball = None

        self.is_paused = False

        self.window.after(16, self.update_game)

    def move_player_paddle_up(self):
        self.left_paddle_movement = -1

    def move_player_paddle_down(self):
        self.left_paddle_movement = 1

    def stop_move_player_paddle_up(self):
        self.left_paddle_movement = 0

    def stop_move_player_paddle_down(self):
        self.left_paddle_movement = 0

    def player_scored(self):
        self.player_score += 1
        self.reset_ball()

    def computer_scored(self):
        self.computer_score += 1
        self.reset_ball()

    def reset_ball(self):
        self.ball_x = 435
        self.ball_y = 235

    def reset_game(self):
        self.player_score = 0
        self.computer_score = 0
        self.left_paddle_x = 50
        self.left_paddle_y = 150
        self.right_paddle_x = 800
        self.right_paddle_y = 150
        self.ball_x = 435
        self.ball_y = 235
        self.ball_movement_x = 1
        self.ball_movement_y = 1

    def change_ball_speed(self, new_ball_speed: int):
        self.ball_speed = new_ball_speed

    def pause(self):
        self.is_paused = True

    def unpause(self):
        self.is_paused = False

    def update_game(self):
        if self.is_paused:
            self.window.after(16, self.update_game)
            return
        self.ball_x += self.ball_movement_x * self.ball_speed
        self.ball_y += self.ball_movement_y * self.ball_speed
        if self.ball_y + self.ball_height >= PongProgram.GAME_HEIGHT or self.ball_y <= 0:
            self.ball_y -= self.ball_movement_y * self.ball_speed
            self.ball_movement_y *= -1
        if self.ball_x <= self.left_paddle_x + self.left_paddle_width and self.ball_x + self.ball_width >= self.left_paddle_x:
            if self.ball_y <= self.left_paddle_y + self.left_paddle_height and self.ball_y + self.ball_height >= self.left_paddle_y:
                horizontal = min(abs(self.ball_x - (self.left_paddle_x + self.left_paddle_width)), abs((self.ball_x + self.ball_width) - self.left_paddle_x))
                vertical = min(abs(self.ball_y - (self.left_paddle_y + self.left_paddle_height)), abs((self.ball_y + self.ball_height) - self.left_paddle_y))
                if horizontal < vertical:
                    self.ball_x -= self.ball_movement_x * self.ball_speed
                    self.ball_movement_x *= -1
                elif vertical < horizontal:
                    self.ball_y -= self.ball_movement_y * self.ball_speed
                    self.ball_movement_y *= -1
                else:
                    self.ball_y -= self.ball_movement_y * self.ball_speed
                    self.ball_movement_y *= -1
                    self.ball_x -= self.ball_movement_x * self.ball_speed
                    self.ball_movement_x *= -1
        if self.ball_x <= self.right_paddle_x + self.right_paddle_width and self.ball_x + self.ball_width >= self.right_paddle_x:
            if self.ball_y <= self.right_paddle_y + self.right_paddle_height and self.ball_y + self.ball_height >= self.right_paddle_y:
                horizontal = min(abs(self.ball_x - (self.right_paddle_x + self.right_paddle_width)), abs((self.ball_x + self.ball_width) - self.right_paddle_x))
                vertical = min(abs(self.ball_y - (self.right_paddle_y + self.right_paddle_height)), abs((self.ball_y + self.ball_height) - self.right_paddle_y))
                if horizontal < vertical:
                    self.ball_y -= self.ball_movement_y * self.ball_speed
                    self.ball_movement_y *= -1
                elif vertical < horizontal:
                    self.ball_x -= self.ball_movement_x * self.ball_speed
                    self.ball_movement_x *= -1
                else:
                    self.ball_y -= self.ball_movement_y * self.ball_speed
                    self.ball_movement_y *= -1
                    self.ball_x -= self.ball_movement_x * self.ball_speed
                    self.ball_movement_x *= -1
        if self.ball_x + self.ball_width <= 0:
            self.computer_scored()
        elif self.ball_x >= PongProgram.GAME_WIDTH:
            self.player_scored()
        self.canvas.moveto(self.ball, self.ball_x, self.ball_y)
        if self.ball_y <= self.right_paddle_y:
            self.right_paddle_movement = -1
        elif self.ball_y >= self.right_paddle_y + self.right_paddle_height:
            self.right_paddle_movement = 1
        else:
            self.right_paddle_movement = 0
        self.left_paddle_y += self.left_paddle_movement
        self.right_paddle_y += self.right_paddle_movement
        self.canvas.moveto(self.left_paddle, self.left_paddle_x, self.left_paddle_y)
        self.canvas.moveto(self.right_paddle, self.right_paddle_x, self.right_paddle_y)
        self.window.after(16, self.update_game)


PongProgram()
