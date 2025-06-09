#include <stdio.h>
#include <string.h>

void vulnerable() {
    char buffer[64];
    printf("Introduce tu mensaje:\n");
    gets(buffer);  // No creo que genere problemas...
    printf("Mensaje recibido: %s\n", buffer);
}

void secreto() {
    printf("¡Lograste redirigir la ejecución!\n");

}

int main() {
    vulnerable();
    return 0;
}

