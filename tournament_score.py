# -*- coding: utf-8 -*-

import bowling


def referee(input, output, rules='local'):
    """
    Подсчитывает количество очков в турнире и объявляет победителя в каждом туре

    :param input: Входной файл с данными об игре
    :param output: Выходной файл с результатом игры
    :return: None
    """
    winner = {}
    input_file = open(input, 'r', encoding='utf8')
    output_file = open(output, 'a', encoding='utf8')
    if rules == 'local':
        scorer = bowling.Scorer
    elif rules == 'global':
        scorer = bowling.GlobalRules
    else:
        raise BaseException('Неизвестные правила игры')
    for line in input_file:
        if line == '\n':
            output_file.write(line)
            continue
        if '###' in line:
            winner = {'name': '', 'score': 0}
            tour = line
            output_file.write(str(line))
            continue
        line = line.rstrip()
        if 'winner' in line:
            output_file.write(line.strip('.') + winner['name'] + '\n')
            continue
        name, result = line.split()
        try:
            score = scorer(result).get_score()
        except BaseException as exc:
            print(f'Exception in {tour}', exc)
            continue
        if score > winner['score']:
            winner['name'] = name
            winner['score'] = score
        output_file.write(f'{name:10}{result:25}{str(score)}\n')
    input_file.close()
    output_file.close()
