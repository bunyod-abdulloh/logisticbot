from aiogram.types import ReplyKeyboardMarkup

admin_uz_main_buttons = ReplyKeyboardMarkup(resize_keyboard=True, one_time_keyboard=True)
admin_uz_main_buttons.row('➕ Admin qo\'shish', '😎 Adminlarni ko\'rish')
admin_uz_main_buttons.row('🚙 Avtomobillar bo\'limi')
admin_uz_main_buttons.row('🏢 Biz haqimizda bo\'limiga matn')
admin_uz_main_buttons.row('📊 Statistika', '👥 Foydalanuvchilar soni')
admin_uz_main_buttons.row('🗣 Foydalanuvchilarga habar yuborish')
admin_uz_main_buttons.row('🏡 Bosh sahifa')

cars_cbuttons = ReplyKeyboardMarkup(resize_keyboard=True, one_time_keyboard=True)
cars_cbuttons.row('🚗 Yengil avtomobillar', '🚚 Yuk avtomobillari')
cars_cbuttons.row('🚜 Qurilish avtomobillari')
cars_cbuttons.row('↩️ Bosh menyuga qaytish')
