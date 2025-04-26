def solution( flowerbed: list[int], n: int) -> bool:
    count = 0
    for x in range(len(flowerbed)):
        if flowerbed[x] == 0:
            prev = flowerbed[0] == 0 or flowerbed[x-1] == 0
            nex = flowebed[x-1] == 0 or flowerbed[x+1] == 0
            if prev and nex:
                flowerbed[x] = 1
                count += 1
                if count >= n:
                    return True
    
        
    return count >= n            


if __name__ == "__main__":
    val = int(input())
    n = int(input())
    flowerbed = [int(input()) for _ in range(val)]
    print(flowerbed)
    result = solution(flowerbed, n)
    print(result)

