/* ************************************************************************** */
/*                                                                            */
/*                                                        :::      ::::::::   */
/*   get_next_line_utils_bonus.c                        :+:      :+:    :+:   */
/*                                                    +:+ +:+         +:+     */
/*   By: meldemir <meldemir@student.42berlin.d      +#+  +:+       +#+        */
/*                                                +#+#+#+#+#+   +#+           */
/*   Created: 2025/12/17 15:58:34 by meldemir          #+#    #+#             */
/*   Updated: 2025/12/17 15:58:38 by meldemir         ###   ########.fr       */
/*                                                                            */
/* ************************************************************************** */

#include "get_next_line_bonus.h"

ssize_t	ft_strchr_index(const char *s, int c, ssize_t len)
{
	ssize_t	i;

	i = 0;
	if (!s) 
		return (-1);
	while (i < len)
	{
		if (s[i] == (char)c)
			return (i);
		i++;
	}
	if (s[i] == (char)c)
		return (i);
	return (-1);
}

char	*ft_substr(char const *s, ssize_t start, ssize_t len)
{
	char	*ptr;
	ssize_t	s_len;

	if (!s)
		return (NULL);
	s_len = ft_strlen(s);
	if (start >= s_len)
	{
		ptr = malloc(1);
		if (!ptr)
			return (NULL);
		ptr[0] = '\0';
		return (ptr);
	}
	if (len > s_len - start)
		len = s_len - start;
	ptr = malloc(len + 1);
	if (!ptr)
		return (NULL);
	ft_strlcpy(ptr, s + start, len + 1);
	return (ptr);
}

ssize_t	ft_strlen(const char *str)
{
	ssize_t	count;

	count = 0;
	while (*str != '\0')
	{
		str++;
		count++;
	}
	return (count);
}

size_t	ft_strlcpy(char *dest, const char *src, size_t size)
{
	size_t	i;
	size_t	cnt;

	i = 0;
	cnt = ft_strlen(src);
	if (size > 0)
	{
		while (src[i] != '\0' && (i < (size - 1)))
		{
			dest[i] = src[i];
			i++;
		}
		dest[i] = '\0';
	}
	return (cnt);
}

size_t	ft_strlcat(char *dest, const char *src, size_t size)
{
	size_t			i;
	size_t			j;
	size_t			srcln;
	size_t			destln;

	destln = 0;
	while (dest[destln] != '\0' && destln < size)
		destln++;
	srcln = ft_strlen(src);
	if (size <= destln)
		return (size + srcln);
	i = destln;
	j = 0;
	while (src[j] != '\0' && i < size - 1)
	{
		dest[i++] = src[j++];
	}
	dest[i] = '\0';
	return (srcln + destln);
}
