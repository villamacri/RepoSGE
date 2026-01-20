
def contador_likes(*likes: int) -> int:
    print(f'{likes=}')
    result=0
    for like in likes:
        result+=like
    return result

print(contador_likes(34, 26, 62, 97, 43))
