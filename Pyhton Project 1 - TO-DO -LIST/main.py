import json
import os


# DATABASE LOGIC (Data Layer)
class TaskDatabase:
    def __init__(self, file_path="todo_data.json"):
        self.file_path = file_path
        self.next_id = 1

        # Initialize internal in-memory shards to distribute database rows
        self.database_shards = {
            "bucket_A": [],
            "bucket_B": [],
            "bucket_C": []
        }

        # Load existing state from disk on startup
        self.load_data()

    def _calculate_bucket(self, task_id):
        """Determine target bucket routing using a simple modulo operation"""
        remainder = task_id % 3
        if remainder == 1:
            return "bucket_A"
        elif remainder == 2:
            return "bucket_B"
        else:
            return "bucket_C"

    def save_task(self, task_text):
        """Construct a structural database row and persist it to disk"""
        if not task_text.strip():
            return False

        # Standard structural key-value database row configuration
        new_row = {
            "id": self.next_id,
            "title": task_text.strip()
        }

        # Route entry into its calculated internal memory shard
        target_bucket = self._calculate_bucket(self.next_id)
        self.database_shards[target_bucket].append(new_row)

        # Increment index pointer and commit storage state to disk
        self.next_id += 1
        self.write_to_disk()
        return True

    def get_all_records(self):
        """Aggregate data rows across all individual buckets
        into a single ordered view"""
        combined = []
        for bucket in self.database_shards.values():
            combined.extend(bucket)

        # Keep items displayed in a sequential order matching database row IDs
        combined.sort(key=lambda item: item["id"])
        return combined

    def write_to_disk(self):
        """Serialize current state memory structures permanently
        onto the filesystem"""
        state_data = {
            "next_id": self.next_id,
            "data": self.database_shards
        }
        with open(self.file_path, "w") as file:
            json.dump(state_data, file, indent=4)

    def load_data(self):
        """Validate state history presence on local disk and safely
        reload structures"""
        if os.path.exists(self.file_path):
            try:
                with open(self.file_path, "r") as file:
                    loaded_state = json.load(file)
                    self.next_id = loaded_state.get("next_id", 1)
                    self.database_shards = loaded_state.get(
                        "data", self.database_shards
                    )
            except (json.JSONDecodeError, KeyError):
                pass


# USER INTERFACE (UI Layer)
def main_menu():
    db = TaskDatabase()

    while True:
        print("\n--- TO-DO ENGINE MENU ---")
        print("1. View All Tasks")
        print("2. Add New Task")
        print("3. Exit Program")

        choice = input("\nOption select karein (1-3): ")

        if choice == "1":
            tasks = db.get_all_records()
            if not tasks:
                print("\n[!] Koi tasks nahi hain. Database khali hai.")
            else:
                print("\n--- APP DATABASE ROWS ---")
                # Pythonic loops using enumerate for safe index
                # and values synchronization
                for num, row in enumerate(tasks, start=1):
                    print(f"{num}. [ID: {row['id']}] -> {row['title']}")

        elif choice == "2":
            user_input = input("Task ka naam likhein: ")
            if db.save_task(user_input):
                print(
                    "[+] Task successfully bucket mein add aur disk par "
                    "save ho gaya."
                )
            else:
                print("[!] Error: Khali text accept nahi kiya ja sakta.")

        elif choice == "3":
            print("\nProcess close ho raha hai. Aap ka data safe hai!")
            break
        else:
            print("[!] Invalid choice. Dobara try karein.")


# MAIN ENTRY POINT
if __name__ == "__main__":
    main_menu()
