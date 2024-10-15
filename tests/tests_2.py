from swarm import Swarm, Agent

client = Swarm()

""" swarm은 단일 에이전트 핸드오프에 최적화 되어 있고, 복잡한 대화 흐름 처리는 어렵다. """

sales_agent = Agent(
    name="Sales",
    instructions="제품 판매와 관련된 문의를 처리하세요. 관련 연락 번호는 070-2222-3333 으로 안내하세요'"
)

billing_agent = Agent(
    name="Billing",
    instructions= "비용 관련 문의를 처리하세요. 컴퓨터 한대는 약 50만원입니다. 그에 맞는 계산을 하여 소비자에게 말하세요."
)

def transfer_to_sales():
    return sales_agent

def transfer_to_billing():
    return billing_agent

customer_service_agent = Agent(
    name="Customer Service",
    instructions="고객 문의를 처리하세요. 구매 관련은 영업팀으로, 비용 관련은 결제팀으로 전달하세요. 그외에는 항상 모른다고 친절하고 공손하게 답변해",
    functions=[transfer_to_sales, transfer_to_billing]
)

response = client.run(
    agent=customer_service_agent,
    messages=[{"role": "user", "content": "컴퓨터 구매하려고 하는데, 어디로 연락하나요? 만약 5대 구매하면 얼마인지도 알려주세요."}],
)

print(response.messages[-1]["content"])


 