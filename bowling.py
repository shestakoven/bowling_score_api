# -*- coding: utf-8 -*-

class Scorer:

    def __init__(self, game_result):
        self.game_result = str(game_result).upper().replace('Х', 'X')
        self.frames = []
        self.prepare()
        self.game_score = 0

    def prepare(self):
        self.check_symbols(self.game_result)
        self.frames = self.make_frames(self.game_result)
        self.check_frames(self.frames)

    def get_score(self):
        for frame in self.frames:
            if frame[0] == 'X':
                self.game_score += 20
            elif frame[1] == '/':
                self.game_score += 15
            else:
                self.game_score += int(frame[0]) + int(frame[1])
        return self.game_score

    def check_symbols(self, string):
        for sym in string:
            if sym not in '-X/123456789':
                raise BaseException(ValueError, 'Результат содержит недопустимые символы')

    def make_frames(self, result):
        frames = []
        throw = []
        result = result.replace('-', '0')
        for sym in result:
            if sym == 'X':
                frames.append([sym])
            else:
                throw.append(sym)
            if len(throw) == 2:
                frames.append(throw)
                throw = []
        return frames

    def check_frames(self, frames):
        if len(frames) != 10:
            raise BaseException(IndexError, 'Количество фреймов должно быть равно десяти!')
        for frame in frames:
            if frame[0] == 'X':
                continue
            elif '/' in frame[0]:
                raise BaseException(ValueError, f'Неверно указан результат: {frame}')
            elif frame[1] == '/':
                continue
            elif int(frame[0]) + int(frame[1]) > 10:
                raise BaseException(ValueError, f'Сумма очков в фрейме не должна превышать 10: {frame}')


class GlobalRules(Scorer):

    def get_score(self):
        game_score = 0
        for i, frame in enumerate(self.frames):
            if frame[0] == 'X':
                self.if_frame_x(frame, i)
            elif frame[1] == '/':
                self.if_frame_spare(frame, i)
            else:
                self.game_score += int(frame[0]) + int(frame[1])
        return self.game_score

    def if_frame_x(self, frame, i):
        if frame[0] == 'X':
            self.game_score += 10
            try:
                if self.frames[i + 1][0] == 'X':
                    self.game_score += 10
                    if self.frames[i + 2][0] == 'X':
                        self.game_score += 10
                    else:
                        self.game_score += int(self.frames[i + 2][0])
                elif self.frames[i + 1][1] == '/':
                    self.game_score += 10
                else:
                    self.game_score += int(self.frames[i + 1][0]) + int(self.frames[i + 1][1])
            except IndexError:
                pass

    def if_frame_spare(self, frame, i):
        if frame[1] == '/':
            self.game_score += 10
            try:
                if self.frames[i + 1][0] == 'X':
                    self.game_score += 10
                else:
                    self.game_score += int(self.frames[i + 1][0])
            except IndexError:
                pass
