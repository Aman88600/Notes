import spacy
from test import put_data

nlp = spacy.load("en_core_web_sm")

KNOWN_TOPICS = {
    "Shopify", "OpenAI", "Reddit", "Duolingo", "Figma", "Trello", "Zoom", "GitLab",
    "Heroku", "DigitalOcean", "MongoDB", "PostgreSQL", "Firebase", "React", "Angular",
    "Vue.js", "Node.js", "Microsoft Azure", "Google Cloud Platform", "Alibaba Cloud"
}

def get_topic(sentence):
    # Getting the input sentence
    doc = nlp(sentence)

    topic_found = False
    for ent in doc.ents:
        if ent.label_ in ["ORG", "PERSON", "PRODUCT"]:
            return ent.text

    # Second try: match known topics from words
    for word in sentence.split():
        if word.strip(".?,") in KNOWN_TOPICS:
            return word


    # Third try: noun chunks (phrases)
    for chunk in doc.noun_chunks:
        chunk_text = chunk.text.strip().title()
        if chunk_text in KNOWN_TOPICS:
            return chunk_text

    return None


user_sentences = [
    "Tell me about Microsoft.",
    "What is Apple Company?",
    "Can you explain Google?",
    "I want to know more about Tesla.",
    "Give me details on Amazon.",
    "Share something about Facebook.",
    "What do you know about Netflix?",
    "Tell me about OpenAI.",
    "What’s the story of Samsung?",
    "Explain IBM.",
    "Tell me more about Intel.",
    "What can you say about Adobe?",
    "I’d like to know about Oracle.",
    "Explain the company SpaceX.",
    "Give me insights into Zoom.",
    "Describe the company Shopify.",
    "Who founded Nvidia?",
    "What’s special about Dell?",
    "Can you elaborate on Twitter?",
    "Give me a summary of PayPal.",
    "Tell me about Airbnb.",
    "What do you know about Uber?",
    "I’m curious about Spotify.",
    "Give me information on ByteDance.",
    "Tell me something about TikTok.",
    "What is Salesforce?",
    "Give a brief about Reddit.",
    "Explain the history of YouTube.",
    "What can you tell me about Huawei?",
    "Tell me more about Alibaba.",
    "What is Pinterest?",
    "Share facts about eBay.",
    "Tell me about LinkedIn.",
    "Can you tell me what Stripe does?",
    "What’s up with Xiaomi?",
    "Describe the company Tencent.",
    "What do you know about Baidu?",
    "Explain what Robinhood is.",
    "Tell me about Discord.",
    "What is Snap Inc.?",
    "What’s the business of Twitch?",
    "Can you give an overview of GitHub?",
    "Tell me about Intel Corporation.",
    "What does HP specialize in?",
    "Tell me something about Dell Technologies.",
    "I’d like to know about IBM.",
    "What’s the role of ARM Holdings?",
    "Tell me more about Palantir.",
    "Can you describe Coinbase?",
    "Give me some information on Reddit.",
    "What exactly is Square?",
    "Explain DoorDash.",
    "What is Instacart?",
    "What do you know about Blue Origin?",
    "What’s the purpose of Kickstarter?",
    "Can you explain Indiegogo?",
    "I want to know about Crunchbase.",
    "Tell me about Khan Academy.",
    "What does Coursera do?",
    "What is edX?",
    "Tell me more about Duolingo.",
    "What’s the mission of Mozilla?",
    "Can you tell me about Notion?",
    "Explain Figma.",
    "Tell me about Canva.",
    "What is Asana?",
    "Tell me about Trello.",
    "What do you know about Monday.com?",
    "Explain the function of Slack.",
    "Tell me about Zoom Video Communications.",
    "What is Atlassian?",
    "Describe JIRA.",
    "What’s GitLab?",
    "Explain what Bitbucket does.",
    "Tell me about DigitalOcean.",
    "What do you know about Heroku?",
    "What is Vercel?",
    "Tell me about Netlify.",
    "What is Firebase?",
    "Can you explain MongoDB?",
    "Tell me about PostgreSQL.",
    "What is Redis used for?",
    "Explain what Elasticsearch is.",
    "Describe Amazon Web Services.",
    "What do you know about Microsoft Azure?",
    "Tell me about Google Cloud Platform.",
    "What is IBM Cloud?",
    "Tell me about Oracle Cloud.",
    "Give me a breakdown of Alibaba Cloud.",
    "What is Cloudflare?",
    "What does Fastly do?",
    "Tell me more about Akamai.",
    "What is Git?",
    "Can you explain Python?",
    "Tell me about the Java programming language.",
    "Explain what JavaScript is.",
    "What is React used for?",
    "Describe Angular.",
    "Tell me about Vue.js.",
    "Explain what Node.js does.",
    "What do you know about TypeScript?",
    "Tell me about C++."
]

# Testing with sentences
if __name__ == "__main__":
    not_found = 0
    for sentence in user_sentences:
        print(sentence)
        topic = get_topic(sentence)
        if topic == None:
            not_found += 1
        print(f"Topic : {topic}")
        put_data(sentence, topic)
    print(f"Misses : {not_found}")