from aiogram.types import ReplyKeyboardMarkup, KeyboardButton

admin_uz_main_buttons = ReplyKeyboardMarkup(resize_keyboard=True)
admin_uz_main_buttons.row('🚙 Avtomobillar bo\'limi')
admin_uz_main_buttons.row('📊 Hisobot', 'Foydalanuvchilar')
admin_uz_main_buttons.row('ID olish', 'ID o\'chirish')
admin_uz_main_buttons.row('↩️ Bosh menyuga qaytish')

cars_cbuttons = ReplyKeyboardMarkup(resize_keyboard=True)
cars_cbuttons.row('Excel shaklda qo\'shish')
cars_cbuttons.row('↩️ Admin menyusiga qaytish')

stats_main = ReplyKeyboardMarkup(resize_keyboard=True)
stats_main.add(KeyboardButton(text='Avtomobillar hisoboti'))
stats_main.add('Logistika hisoboti')
stats_main.add('Xaridlar hisoboti')
stats_main.add('Barchasini yuklab olish')
stats_main.add('↩️ Admin menyusiga qaytish')

admin_users_button = ReplyKeyboardMarkup(resize_keyboard=True)
admin_users_button.row('👥 Foydalanuvchilar soni')
admin_users_button.row('🗣 Foydalanuvchilarga habar yuborish')
admin_users_button.row('Download all users')
admin_users_button.row('Block user', 'Unblock user')
admin_users_button.row('↩️ Admin menyusiga qaytish')
