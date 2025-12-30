/* ************************************************************************** */
/*                                                                            */
/*                                                        :::      ::::::::   */
/*   ft_strmapi.c                                       :+:      :+:    :+:   */
/*                                                    +:+ +:+         +:+     */
/*   By: meldemir <meldemir@student.42berlin.d      +#+  +:+       +#+        */
/*                                                +#+#+#+#+#+   +#+           */
/*   Created: 2025/11/28 14:28:38 by meldemir          #+#    #+#             */
/*   Updated: 2025/11/28 14:28:40 by meldemir         ###   ########.fr       */
/*                                                                            */
/* ************************************************************************** */
#include "libft.h"

char	*ft_strmapi(char const *s, char (*f)(unsigned int, char))
{
	char	*s_new;
	size_t	s_len;
	size_t	i;

	i = 0;
	s_len = ft_strlen(s);
	s_new = malloc(s_len + 1);
	if (!s_new)
		return (NULL);
	while (i < s_len)
	{
		s_new[i] = (*f)(i, s[i]);
		i++;
	}
	s_new[i] = '\0';
	return (s_new);
}
/*
#include <stdlib.h>
#include <unistd.h>
#include <string.h>

void	ft_print_result(char const *s)
{
	int		len;

	len = 0;
	while (s[len])
		len++;
	write(1, s, len);
}

char	mapi(unsigned int i, char c)
{
	static int indexArray[11] = {0};

	if (i > 10 || indexArray[i] == 1)
		write(1, "wrong index\n", 12);
	else
		indexArray[i] = 1;
	if (c >= 'a' && c <= 'z')
		return (c - 32);
	else if (c >= 'A' && c <= 'Z')
		return (c + 32);
	else
		return (c);
}

int		main(int argc, const char *argv[])
{
	char	*str;
	char	*strmapi;

	alarm(5);
	str = (char *)malloc(sizeof(*str) * 12);
	if (argc == 1 || !str)
		return (0);
	else if (atoi(argv[1]) == 1)
	{
		strcpy(str, "LoReM iPsUm");
		strmapi = ft_strmapi(str, &mapi);
		ft_print_result(strmapi);
		if (strmapi == str)
			ft_print_result("\nA new string was not returned");
		if (strmapi[11] != '\0')
			ft_print_result("\nString is not null terminated");
	}
	return (0);
}
	*/