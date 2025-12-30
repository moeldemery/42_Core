/* ************************************************************************** */
/*                                                                            */
/*                                                        :::      ::::::::   */
/*   ft_split.c                                         :+:      :+:    :+:   */
/*                                                    +:+ +:+         +:+     */
/*   By: meldemir <meldemir@student.42berlin.d      +#+  +:+       +#+        */
/*                                                +#+#+#+#+#+   +#+           */
/*   Created: 2025/11/28 07:51:27 by meldemir          #+#    #+#             */
/*   Updated: 2025/11/28 07:51:29 by meldemir         ###   ########.fr       */
/*                                                                            */
/* ************************************************************************** */
#include "libft.h"

static size_t	ft_strcountmatch(const char *s, int c)
{
	size_t	i;
	size_t	n;
	int		is_match;

	i = 0;
	n = 0;
	is_match = 0;
	while (s[i])
	{
		if (s[i] != (char)c)
		{
			if (!is_match)
			{
				is_match = 1;
				n++;
			}
		}
		else
			is_match = 0;
		i++;
	}
	return (n);
}

char	**ft_split(char const *s, char c)
{
	char	**ptrarr;
	size_t	len;
	size_t	i;

	i = 0;
	if (!s)
		return (NULL);
	ptrarr = (void *)malloc(sizeof(char *) * (ft_strcountmatch(s, (int)c) + 1));
	if (!ptrarr)
		return (NULL);
	while (*s)
	{
		if (*s != c)
		{
			len = 0;
			while (*s && *s != c && ++len)
				s++;
			ptrarr[i++] = ft_substr(s - len, 0, len);
		}
		else
			s++;
	}
	ptrarr[i] = NULL;
	return (ptrarr);
}

/*
#include <stdlib.h>
#include <unistd.h>
#include "../../../libft.h"

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
	char	**tabstr;
	int		i;
	int		arg;

	alarm(5);
	if (argc == 1)
		return (0);
	i = 0;
	if ((arg = atoi(argv[1])) == 1)
	{
		if (!(tabstr = ft_split("          ", ' ')))
			ft_print_result("NULL");
		else
		{
			while (tabstr[i] != NULL)
			{
				ft_print_result(tabstr[i]);
				write(1, "\n", 1);
				i++;
			}
		}
	}
	else if (arg == 2)
	{
		if (!(tabstr = ft_split("lorem ipsum dolor sit 
		amet, consectetur adipiscing elit. Sed non 
		risus. Suspendisse", ' ')))
			ft_print_result("NULL");
		else
		{
			while (tabstr[i] != NULL)
			{
				ft_print_result(tabstr[i]);
				write(1, "\n", 1);
				i++;
			}
		}
	}
	else if (arg == 3)
	{
		if (!(tabstr = ft_split("   lorem   ipsum 
		dolor     sit amet, consectetur   adipiscing elit. 
		Sed non risus. Suspendisse   ", ' ')))
			ft_print_result("NULL");
		else
		{
			while (tabstr[i] != NULL)
			{
				ft_print_result(tabstr[i]);
				write(1, "\n", 1);
				i++;
			}
		}
	}
	else if (arg == 4)
	{
		if (!(tabstr = ft_split("lorem ipsum dolor 
		sit amet, consectetur adipiscing elit. Sed 
		non risus. Suspendisse lectus tortor, dignissim 
		sit amet, adipiscing nec, ultricies sed, dolor. 
		Cras elementum ultricies diam. Maecenas ligula 
		massa, varius a, semper congue, euismod non, mi.", 'i')))
			ft_print_result("NULL");
		else
		{
			while (tabstr[i] != NULL)
			{
				ft_print_result(tabstr[i]);
				write(1, "\n", 1);
				i++;
			}
		}
	}
	else if (arg == 5)
	{
		if (!(tabstr = ft_split("lorem ipsum 
		dolor sit amet, consectetur adipiscing 
		elit. Sed non risus. Suspendisse lectus 
		tortor, dignissim sit amet, adipiscing 
		nec, ultricies sed, dolor. Cras elementum 
		ultricies diam. Maecenas ligula massa, varius 
		a, semper congue, euismod non, mi.", 'z')))
			ft_print_result("NULL");
		else
		{
			while (tabstr[i] != NULL)
			{
				ft_print_result(tabstr[i]);
				write(1, "\n", 1);
				i++;
			}
		}
	}
	else if (arg == 6)
	{
		if (!(tabstr = ft_split("", 'z')))
			ft_print_result("NULL");
		else
			if (!tabstr[0])
				ft_print_result("ok\n");
	}
	return (0);
}
*/