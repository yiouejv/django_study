# #encoding: utf-8
#
# #
# # def bubble_sort(l):
# #     for i in range(len(l)-1):  # 控制循环的次数
# #         for j in range(0, len(l)-1):
# #             if l[j] < l[j+1]:
# #                 l[j], l[j+1] = l[j+1], l[j]
# #     return l
# #
# #
# # def main():
# #     l = [1, 3, 2, 1, 5, 6, 7, 3]
# #     l = bubble_sort(l)
# #     print(l)
# #
# #
# # if __name__ == '__main__':
# #     main()
#
# l = [1, 2, 3, 1, 2, 2, 4, 4]
# def bubble(l):
#     for i in range(len(l)-1):
#         for j in range(len(l)-1):
#             if l[j] < l[j+1]:
#                 l[j], l[j+1] = l[j+1], l[j]
#     return l
# print(bubble(l))