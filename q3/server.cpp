#include <unistd.h>
#include <stdio.h>
#include <stdlib.h>
#include <sys/socket.h>
#include <stdlib.h>
#include <netinet/in.h>
#include <string.h>

#define PORT 2999

int main(int argc, char const *argv[])
{
    int server_fd, new_socket, valread;
    struct sockaddr_in address;
    int opt = 1;
    int addrlen = sizeof(address);

    char in_buffer[1024] = {0};
    char *out_buffer;
    size_t size = 0;

    // Creating socket file descriptor
    if ((server_fd = socket(AF_INET, SOCK_STREAM, 0)) == 0)
    {
        perror("socket failed");
        exit(EXIT_FAILURE);
    }

    // Attaching socket to the port 2999
    if (setsockopt(server_fd, SOL_SOCKET, SO_REUSEADDR | SO_REUSEPORT, &opt, sizeof(opt)))
    {
        perror("setsockopt");
        exit(EXIT_FAILURE);
    }

    address.sin_family = AF_INET;
    address.sin_addr.s_addr = INADDR_ANY;
    address.sin_port = htons( PORT );

    // Binding socket to the port 8080
    if (bind(server_fd, (struct sockaddr *)&address, sizeof(address))<0)
    {
        perror("bind failed");
        exit(EXIT_FAILURE);
    }
    if (listen(server_fd, 3) < 0)
    {
        perror("listen");
        exit(EXIT_FAILURE);
    }
    if ((new_socket = accept(server_fd, (struct sockaddr *)&address, (socklen_t*)&addrlen))<0)
    {
        perror("accept");
        exit(EXIT_FAILURE);
    }

    valread = read(new_socket, in_buffer, 1024);
    printf("%s\n", in_buffer);

    // Executing the script
    system("../q1.sh www.usec.io Ninja>q1.out");

    FILE *fp = fopen("q1.out", "r");
    fseek(fp, 0, SEEK_END);
    
    size = ftell(fp);

    rewind(fp);

    out_buffer = (char *)malloc((size + 1) * sizeof(*out_buffer));
    fread(out_buffer, size, 1, fp);
    out_buffer[size] = '\0';

    send(new_socket, out_buffer, strlen(out_buffer), 0);
    return 0;
}
