#include <stdio.h>
#include <stdlib.h>
#include <time.h>

int main() {
    int X, Y;

    printf("Введите ширину карты (X): ");
    scanf("%d", &X);
    printf("Введите высоту карты (Y): ");
    scanf("%d", &Y);


    // Проверка на корректные размеры
    if (X <= 0 || Y <= 0 || X > 50 || Y > 50) {
        printf("Неверные размеры карты. Используйте значения от 1 до 50.\n");
        return 1; //Возвращаем код ошибки
    }


    char **map = (char **)malloc(Y * sizeof(char *));
    for (int i = 0; i < Y; i++) {
        map[i] = (char *)malloc(X * sizeof(char));
    }

    srand(time(NULL));

    for (int i = 0; i < Y; i++) {
        for (int j = 0; j < X; j++) {
            int random_type = rand() % 4;
            switch (random_type) {
                case 0: map[i][j] = '.'; break;
                case 1: map[i][j] = '#'; break;
                case 2: map[i][j] = '~'; break;
                case 3: map[i][j] = '*'; break;
                default: map[i][j] = ' '; break;
            }
        }
    }

    for (int i = 0; i < Y; i++) {
        for (int j = 0; j < X; j++) {
            printf("%c ", map[i][j]);
        }
        printf("\n");
    }

    // Освобождение выделенной памяти
    for (int i = 0; i < Y; i++) {
        free(map[i]);
    }
    free(map);

    return 0;
}
