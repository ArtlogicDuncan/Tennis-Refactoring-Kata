class TennisGame1:
    def __init__(self, player1_name, player2_name):
        self.player1_name = player1_name
        self.player2_name = player2_name
        self.player1_points = 0
        self.player2_points = 0

    def won_point(self, player_name):
        if player_name == "player1":
            self.player1_points += 1
        else:
            self.player2_points += 1

    def score(self):
        result = ""
        temp_score = 0
        points_difference = self.player1_points - self.player2_points
        if points_difference == 0:
            result = self.__score_is_equal()
        elif self.player1_points >= 4 or self.player2_points >= 4:
            result = self.__is_win_or_advantage(points_difference)
        else:
            for i in range(1, 3):
                if i == 1:
                    temp_score = self.player1_points
                else:
                    result += "-"
                    temp_score = self.player2_points
                result += {
                    0: "Love",
                    1: "Fifteen",
                    2: "Thirty",
                    3: "Forty",
                }[temp_score]
        return result

    def __score_is_equal(self):
        result = {
            0: "Love-All",
            1: "Fifteen-All",
            2: "Thirty-All",
        }.get(self.player1_points, "Deuce")
        return result

    def __is_win_or_advantage(self, points_difference):
        if points_difference == 1:
            result = "Advantage player1"
        elif points_difference == -1:
            result = "Advantage player2"
        elif points_difference >= 2:
            result = "Win for player1"
        else:
            result = "Win for player2"
        return result
