#include <stdio.h>
#include <unistd.h>

int infinite_while(void);

/**
 * main - creates 5 zombie processes
 *
 * Return: 0
 */
int main(void)
{
	int i, pid;

	for (i = 0; i < 5; i++)
	{
		pid = fork();
		if (pid > 0)
			printf("Zombie process created, PID: %d\n", pid);
		else
			return (0);
	}
	infinite_while();
	return (0);
}

/**
 * infinite_while - to keep process running
 *
 * Return: 0
 */
int infinite_while(void)
{
	while (1)
	{
		sleep(1);
	}
	return (0);
}
