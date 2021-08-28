# Powered By Neko.vecter
# The method library for Python Programming class

age_list = []
score_list = []
 
unique_age_list = []
score_age_list = []
times_age_list = []

bubbles_sort_age_list = []
bubbles_sort_score_list = []
bubbles_sort_times_list = []

class method_lib():
    
    def __init__(self):
        super().__init__()
    

    #method for add
    def add_new_e(self, age, score):
        age_list.append(age)
        score_list.append(score)
        print("Finsh add element:" , "age:" , age , "score:" , score)

        pass

    # del last element from list
    def remove_old_e(self):
        age_list.pop(-1)
        score_list.pop(-1)
        print("finsh del last element")

        pass

    # calculate 
    def times_age(self):
        list_age = age_list # make a list only used this function
        score_list_p = score_list
        unique = [] # The list know how mach time
        score = []
        times = []

        global unique_age_list # make unique_age_list be global var
        global score_age_list # make score_age_list be global var
        global times_age_list # make times_age_list be global var
        s_temp = 0
        for i in range(len(list_age)):
            f = 0
            for j in range(len(unique)):
                if(list_age[i] == unique[j]):
                    f = 1
                    score[j] = ((score[j] * times[j]) + score_list_p[i]) / (times[j]+1)
                    times[j] = times[j] + 1
                
                    break
            if(f == 0):
                unique.append(list_age[i])
                score.append(score_list[i])
                times.append(1)
            

        unique_age_list = unique.copy()
        score_age_list = score
        times_age_list = times
    
        return unique ,score , times

    # return only unique_age_list
    def request_unique_age_list(self):
        return unique_age_list

    def request_score_age_list(self):
        return score_age_list

    # return only times_age_list
    def request_times_age_list(self):
        return times_age_list

    # print age_list element
    def s_age_list(self):
        print(age_list)
        return age_list

    # print num_list element
    def s_num_list():
        print(score_list)
        return score_list

    # Bubbles sort method
    def bubbles_sort_age(self):
        nums = unique_age_list
        score = score_age_list
        times = times_age_list

        for i in range(len(nums) - 1):
            for j in range(len(nums) - i - 1):
                if nums[j] > nums[j + 1]:
                    nums[j], nums[j + 1] = nums[j + 1], nums[j]
                    times[j], times[j + 1] = times[j + 1], times[j]
                    score[j], score[j + 1] = score[j + 1], score[j]

        global bubbles_sort_age_list
        global bubbles_sort_score_list
        global bubbles_sort_times_list

        bubbles_sort_age_list = nums
        bubbles_sort_score_list = score
        bubbles_sort_times_list = times

        print("finish bubbles sort")
        return bubbles_sort_age_list, bubbles_sort_score_list, bubbles_sort_times_list

    # Return bubbles unique age list
    def request_bubbles_unique_age_list(self):
        return bubbles_sort_age_list

    # Return bubbles score list
    def request_bubbles_sort_score_list(self):
        return bubbles_sort_score_list

    # Return bubbles age appear list
    def request_bubbles_times_age_list(self):
        return bubbles_sort_times_list

    # Calculate the average of all ages
    def avg_s(self, score, times):
        num_p = score
        times_p = times
        counter_obj = 0
        counter_times = 0
        for i in range(len(score)):
            counter_obj += num_p[i]
            counter_times += times_p[i]

        avg = counter_obj/counter_times

        return avg

    # Calculate the average of each age score separately
    def avg_s_age(self, age, score, times):
        age_p = age
        num_p = score
        times_p = times
        avg_list = []
        temp = 0

        for i in range(len(age_p)):
            avg_list.append(num_p[i]/times_p[i])
    
        return avg_list