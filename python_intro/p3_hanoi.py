disknum = input('Enter the number of disks : ')

def hanoi(n,start,to,other):
    n == disknum
    if n == 0:
        return
    hanoi(n - 1, start, other, to)
    print('Disk Move {} => {}'.format(start, to))
    hanoi(n - 1, other, to, start)

hanoi(4,'A','C','B')

# H(1,A,C) 1개의 디스크를 A B C에 해당하는 Pole A에서 C로 옮긴다. 재귀함수는 항상 논리를 먼저 설게해야 함
#대칭의 논리로 H(1,A,C) == H(1,A,B) == H(1,A,C) 하나의 디스크를 계속 옮기는건 쉬움
#디스크 1개짜리 H(2,A,C) == H(2,A,B) == H(2,B,C)
#디스크 2개짜리 H(3,A,C) == H(3,A,B) == H(3,B,C) 디스크 3개를 A에서 C로 보내거나 할 수 있음. 하지만 가장 큰 디스크가 가장 아래임.
#어떤 문제든 간에 첫번째 pole에 가장 큰 디스크가 있고, 가운데에 모든 디스크가 위에서 작은 크기 순서대로 배치 되어 있어야 함.
#H(4,A,C) 풀이법
#H(3,A,B) -> A에서 C로 보내기 -> H(3,B,C)-> B에서 C로 옮기기. 그런데 저것들은 다 위에서 할 수 있다고 적어 놓은 부분임.
# 크게 두번 옮긴다.
# 1. 일단 n-1까지를 출발 기둥(Start)에서 중간 기둥(Waypoint)을 거쳐 도착 기동(Destination)으로 옮긴다.
# 2. 그리고 출발 기둥(Start)에 남아있는 n번째(제일 큰) 원판을 도착 기동(Destination)기둥으로 바로 옯긴다.
# 3. 중간 기둥(Waypoint)에 남아있는 n-1까지들을 다시 출발 기둥(Start)를 겨처 도착 기동(Destination)으로 옮긴다.

# 하노이 타워를 점화식으로 표현한 것이다.
# -> H(n,A,C)
# 1. H(n-1,A,B)
# 2. A -> C
# 3. H(n-1,B,C)
