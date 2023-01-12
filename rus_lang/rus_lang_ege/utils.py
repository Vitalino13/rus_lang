def remove_token_key(reply):
    """Функция принимает объект request.POST.

    Возвращаетсловарь с удаленным ключом 'csrfmiddlewaretoken'."""
    for item in reply:
        if item[0] == 'csrfmiddlewaretoken':
            reply.remove(item)
    return reply


def create_message(score: int, total: int) -> str:
    """Функция создает текстовое представление результатов."""
    return (f"Вы набрали {score} баллов из {total} возможных")


def convert_to_dict(bd):
    bd_dict = {}
    for tup in bd:
        bd_dict.setdefault(tup[0], []).append(tup[1:])
    return bd_dict


def check_answer(reply, bd):
    ls = {}
    for tup in reply:
        answers = []
        q_id = int(tup[0])
        cor = bd[q_id]
        for num in tup[1]:
            for ans in cor:
                if int(num) == ans[0]:
                    answers.append((num, ans[1]))
        ls[q_id] = answers
    return ls

