#ДЕКОРАТОРЫ
# def user(person_description):
#      def user_name(*args):
#           print('Nazar')
#           person_description(*args)
#      return user_name
     
# @user
# def user_year(year):
#      print('was born in', 2007)

# @user
# def user_job(job):
#      print('3d designer job')

# user_year(2007)
# user_job('3d designer job')

# def site(header):
#      def footer(*args):
#         catalog = input('Your type?')
#         if catalog == 'sport' or 'toys' or 'games' or 'food and snack':
#             result = header(*args)
#             return result
#         header (catalog)
#      return footer

# @site
# def site_photo(photo):
#     print('this photo abaut....')

# def user(a, b):
#     if a > 100:
#         return a % b
#     elif a < 100:
#         return a
    
# result = user(int(input('your think price:')), int(input(':')))
# print(result)
    
# site_photo('photo')
# user('your price and discount')