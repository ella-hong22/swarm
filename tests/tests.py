from swarm import Swarm, Agent

client = Swarm()

def transfer_to_k():
    return k_pop

def transfer_to_j():
    return j_pop

def transfer_to_us():
    return us_pop


main_agent = Agent(
    name="main_agent",
    instructions="You are a helpful agent. If the user asks about k-pop, transfer them to transfer_to_k. if the user asks about j-pop, transfer them to transfer_to_j. if the user asks about us-pop, transfer them to transfer_to_us.",
    functions=[transfer_to_k, transfer_to_j, transfer_to_us],
)

j_pop = Agent(
    name="j_pop",
    instructions="Only speak in japaness. 나는 일본의 k-pop에 대해 잘 알고 있어. 그리고 항상 마지막에 '일본이좋아' 이라고 말해",
)

us_pop = Agent(
    name="us_pop",
    instructions="Only speak in english. 나는 미국의 us-pop에 대해 잘 알고 있어. 그리고 항상 마지막에 '미국이좋아' 이라고 말해",
)

k_pop = Agent(
    name="k_pop",
    instructions="Only speak in korean. 나는 한국의 k-pop에 대해 잘 알고 있어. 그리고 항상 마지막에 '한국이좋아' 이라고 말해"
)

response = client.run(
    agent=main_agent,
    messages=[{"role": "user", "content": "안녕 너 bts 잘 알아? 그리고 한국이랑 일본 노래 좀 추천해줘. 미국노래는? "}],
)

print(response.messages[-1]["content"])