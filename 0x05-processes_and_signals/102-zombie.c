#include <stdio.h>
#include <stdlib.h>
#include <unistd.h>

/**
 * perpetual_pause - Executes an endless loop that pauses execution periodically.
 *
 * Return: This function never returns.
 */
int perpetual_pause(void)
{
    while (1)
    {
        sleep(1); // Pause the program for 1 second to reduce CPU usage.
    }
}

/**
 * main - Initiates the creation of multiple zombie processes.
 *
 * Description: Generates five zombie processes, then runs an infinite loop.
 * Each zombie's PID is printed to the console.
 *
 * Return: Always returns EXIT_SUCCESS.
 */
int main(void)
{
    pid_t child_pid;
    int num_zombies = 0;

    while (num_zombies < 5)
    {
        child_pid = fork();
        if (child_pid > 0) // Parent process
        {
            printf("Created a zombie process with PID: %d\n", child_pid);
            sleep(1);  // Wait a bit before creating another zombie
            num_zombies++;
        }
        else
        {
            exit(0); // Child process exits immediately, becoming a zombie
        }
    }

    perpetual_pause(); // Engage in an infinite sleep loop
    return (EXIT_SUCCESS);
}
