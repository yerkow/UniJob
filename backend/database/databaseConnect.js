// filepath: c:\Users\user\Desktop\projects\UniJob\backend\database\databaseConnect.js

import { Sequelize } from 'sequelize';
import dotenv from 'dotenv';

dotenv.config(); // Загружаем переменные из .env

// Настройки подключения
const sequelize = new Sequelize(
  process.env.DB_NAME,
  process.env.DB_USER,
  process.env.DB_PASSWORD,
  {
    host: process.env.DB_HOST,
    
  }
);

// Проверка подключения
const connectToDatabase = async () => {
  try {
    await sequelize.authenticate();
    console.log('Успешное подключение к базе данных через Sequelize');
  } catch (error) {
    console.error('Ошибка подключения к базе данных:', error.message);
  }
};

connectToDatabase();

export default sequelize;

