# 과제 2. 가장 효율적인 해저 케이블망을 구성하고 제거된 케이블망의 가중치를 출력하라. (응용예제 02)
# 출력 예시
# ## 해저 케이블 연결을 위한 전체 연결도 ##
#  	서울	뉴욕	런던	북경	방콕	파리	
# 서울	0	80	0	10	0	0	
# 뉴욕	80	0	0	40	70	0	
# 런던	0	0	0	0	30	60	
# 북경	10	40	0	0	50	0	
# 방콕	0	70	30	50	0	20	
# 파리	0	0	60	0	20	0	

# ## 가장 효율적인 해저 케이블 연결도 ##
#  	서울	뉴욕	런던	북경	방콕	파리	
# 서울	0	80	0	0	0	0	
# 뉴욕	80	0	0	0	70	0	
# 런던	0	0	0	0	30	60	
# 북경	0	0	0	0	50	0	
# 방콕	0	70	30	50	0	0	
# 파리	0	0	60	0	0	0
# 제거된 케이블: [10, 20, 40]
class Graph():
    def __init__ (self, size):
        self.SIZE = size
        self.graph = [[0 for _ in range(size)] for _ in range(size)]


def print_graph(g, cityAry):
    # 코드 작성 구간: 그래프 출력 (정점 정보 포함, print 함수 사용 시 end='\t')


def find_vertex(g, find_vtx):
    stack = []  # 스택 초기화
    visitedAry = []  # 방문한 정점 초기화
    current = 0  # 시작 정점
    stack.append(current)
    visitedAry.append(current)
    # 코드 작성 구간: 정점 탐색(그래프 깊이 우선 탐색)


    if find_vtx in visitedAry:
        return True  # 정점 연결 True
    else:
        return False  # 정점 연결 False
    


def efficient_cable_networks(g):
    # 반환할 리스트 생성
    remove = []

    # 코드 작성 구간: 최대 비용(높은 네트워크 속도) 신장 트리
    
    # 가중치 간선 배열 생성

    # item 0번째 기준(가중치)으로 오름차순 정렬

    # 갱신할 가중치 간선 배열 생성(중복 제거)

    # 가중치가 낮은 간선부터 제거 (반복)

    return remove


# 실행 구문 (아래 코드를 수정하지 마시오.)
cityAry = ['서울', '뉴욕', '런던', '북경', '방콕', '파리' ]  # 도시 배열
서울, 뉴욕, 런던, 북경, 방콕, 파리 = 0, 1, 2, 3, 4, 5  # 도시, 수치 매핑

G1 = Graph(6)  # 빈 그래프 생성
G1.graph[서울][뉴욕] = 80; G1.graph[서울][북경] = 10
G1.graph[뉴욕][서울] = 80; G1.graph[뉴욕][북경] = 40; G1.graph[뉴욕][방콕] = 70
G1.graph[런던][방콕] = 30; G1.graph[런던][파리] = 60
G1.graph[북경][서울] = 10; G1.graph[북경][뉴욕] = 40; G1.graph[북경][방콕] = 50
G1.graph[방콕][뉴욕] = 70; G1.graph[방콕][북경] = 50; G1.graph[방콕][런던] = 30; G1.graph[방콕][파리] = 20
G1.graph[파리][방콕] = 20; G1.graph[파리][런던] = 60;

print('## 해저 케이블 연결을 위한 전체 연결도 ##')
print_graph(G1, cityAry)  # 그래프 출력

print('## 가장 효율적인 해저 케이블 연결도 ##')
total = efficient_cable_networks(G1)  # 효율적인 해저 케이블 생성과 제거된 케이블 반환
print_graph(G1, cityAry)  # 그래프 출력
print('## 제거된 케이블: ', total)