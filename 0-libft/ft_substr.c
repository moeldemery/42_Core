/* ************************************************************************** */
/*                                                                            */
/*                                                        :::      ::::::::   */
/*   ft_substr.c                                        :+:      :+:    :+:   */
/*                                                    +:+ +:+         +:+     */
/*   By: meldemir <meldemir@student.42berlin.d      +#+  +:+       +#+        */
/*                                                +#+#+#+#+#+   +#+           */
/*   Created: 2025/11/28 02:24:26 by meldemir          #+#    #+#             */
/*   Updated: 2025/11/28 02:24:29 by meldemir         ###   ########.fr       */
/*                                                                            */
/* ************************************************************************** */
#include "libft.h"

char	*ft_substr(char const *s, unsigned int start, size_t len)
{
	void	*ptr;
	size_t	sub_len;

	if (!s)
		return (NULL);
	if (start > ft_strlen(s))
		sub_len = 0;
	else if (len > ft_strlen(s + start))
		sub_len = ft_strlen(s + start);
	else
		sub_len = len;
	ptr = (void *)malloc(sub_len + 1);
	if (!ptr)
		return (NULL);
	ft_strlcpy (ptr, (s + start), sub_len + 1);
	return (ptr);
}

/*
#include <stdlib.h>
#include <unistd.h>

void	ft_print_result(char const *s)
{
	int		len;

	len = 0;
	while (s[len])
		len++;
	write(1, s, len);
}

int		main(int argc, const char *argv[])
{
	char	str[] = "lorem ipsum dolor sit amet";
	char	*strsub;
	int		arg;

	alarm(5);
	if (argc == 1)
		return (0);
	else if ((arg = atoi(argv[1])) == 1)
	{
		if (!(strsub = ft_substr(str, 0, 10)))
			ft_print_result("NULL");
		else
			ft_print_result(strsub);
		if (str == strsub)
			ft_print_result("\nA new string was not returned");
	}
	else if (arg == 2)
	{
		if (!(strsub = ft_substr(str, 7, 10)))
			ft_print_result("NULL");
		else
			ft_print_result(strsub);
		if (str == strsub)
			ft_print_result("\nA new string was not returned");
	}
	else if (arg == 3)
	{
		if (!(strsub = ft_substr(str, 7, 0)))
			ft_print_result("NULL");
		else
			ft_print_result(strsub);
		if (str == strsub)
			ft_print_result("\nA new string was not returned");
	}
	else if (arg == 4)
	{
		if (!(strsub = ft_substr(str, 0, 0)))
			ft_print_result("NULL");
		else
			ft_print_result(strsub);
		if (str == strsub)
			ft_print_result("\nA new string was not returned");
	}
	else if (arg == 5)
	{
		char *bullshit;
		if (!(strsub = ft_substr(str, 400, 20)))
			ft_print_result("NULL");
		else
		{
			bullshit = (char *)&strsub[30];
			bullshit = "FULL BULLSHIT";
			if (strsub)
				ft_print_result(strsub);
			else
				ft_print_result("rip");
		}
		if (str == strsub)
			ft_print_result("\nA new string was not returned");
		(void)bullshit;
	}
	return (0);
}
    */