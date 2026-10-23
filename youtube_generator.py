import random
import datetime

class YouTubeNameGenerator:
    def __init__(self):
        self.styles = {
            "pro": ["{topic} {name} Official", "{name} | {topic} Pro", "The {topic} Lab with {name}"],
            "fun": ["{name} & {topic} Fun", "Crazy {topic} with {name}", "{name}'s {topic} World"],
            "short": ["{topic}{name}", "{name}{topic}", "{topic}X{name}"]
        }

    def generate_names(self, name, topic, count=10):
        print(f"\n🚀 Generating {count} professional ideas for: {name} + {topic}\n")
        print("="*50)
        results = []
        
        for i in range(count):
            style_key = random.choice(list(self.styles.keys()))
            template = random.choice(self.styles[style_key])
            channel_name = template.format(name=name.strip().title(), topic=topic.strip().title())
            results.append(channel_name)
            print(f"{i+1}. {channel_name}  [{style_key.upper()}]")
        
        print("="*50)
        self.save_to_file(name, topic, results)
        return results

    def save_to_file(self, name, topic, results):
        filename = f"channel_ideas_{name}.txt"
        with open(filename, "w", encoding="utf-8") as f:
            f.write(f"YouTube Channel Ideas - {datetime.datetime.now()}\n")
            f.write(f"Nickname: {name}\nTopic: {topic}\n\n")
            for r in results:
                f.write(r + "\n")
        print(f"\n✅ تم حفظ كل الاقتراحات في ملف: {filename}")

def main():
    print("="*50)
    print("  Welcome to YouTube Channel Name Generator PRO v2.0")
    print("  Developed by Murtaza Alseed")
    print("="*50)
    
    name = input("\nWhat is your nickname? \n> ")
    topic = input("What is your channel about? (e.g. Gaming, Tech) \n> ")

    if not name or not topic:
        print("❌ Error: Name and Topic cannot be empty!")
        return

    generator = YouTubeNameGenerator()
    generator.generate_names(name, topic, count=15)

if __name__ == "__main__":
    main()
