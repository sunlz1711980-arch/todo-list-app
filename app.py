# Danh sách để lưu các công việc
tasks = []
def add_task(task_name):
    cong_viec = {'name':"Tên công việc",'completed':False}
    """Thêm một công việc mới vào danh sách."""
    cong_viec ['name'] = task_name
    tasks.append(cong_viec)
    print(f"Đã thêm công việc: '{task_name}'")
def complete_task(task_index):
    tasks[task_index]['completed'] = True
def list_tasks():
    for i in range(len(tasks)):
        if tasks[i] ['completed']==True:
            print('[X]', tasks[i]['name'])
        else:
            print( '[ ]',tasks[i]['name'])
# --- Điểm bắt đầu của chương trình ---
if __name__ == "__main__":
    print("Chào mừng đến với ứng dụng To-Do List!")
    add_task("Học bài Git và GitHub")
    add_task("Làm bài tập thực hành ở nhà")
    complete_task(0)
    list_tasks()
