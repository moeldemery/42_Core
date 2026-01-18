/* ************************************************************************** */
/*                                                                            */
/*                                                        :::      ::::::::   */
/*   get_next_line_bonus.h                              :+:      :+:    :+:   */
/*                                                    +:+ +:+         +:+     */
/*   By: meldemir <meldemir@student.42berlin.d      +#+  +:+       +#+        */
/*                                                +#+#+#+#+#+   +#+           */
/*   Created: 2025/12/17 15:58:02 by meldemir          #+#    #+#             */
/*   Updated: 2025/12/17 15:58:07 by meldemir         ###   ########.fr       */
/*                                                                            */
/* ************************************************************************** */

#ifndef GET_NEXT_LINE_BONUS_H
# define GET_NEXT_LINE_BONUS_H

# include <stdlib.h>
# include <unistd.h>

# ifndef BUFFER_SIZE
#  define BUFFER_SIZE 42
# endif
# define FD_MAX_NUMBER 1024

char	*_create_empty_buffer(char **buffer);
char	*_check_buffer(char **buffer);
char	*_merge_buffer(char **buffer, char *buf_read);
int		_fill_buffer(char **buffer, int fd);
char	*_get_line(char **buf, int newline_index);
char	*get_next_line(int fd);

ssize_t	ft_strchr_index(const char *s, int c, ssize_t len);
char	*ft_substr(char const *s, ssize_t start, ssize_t len);
ssize_t	ft_strlen(const char *str);
size_t	ft_strlcpy(char *dest, const char *src, size_t size);
size_t	ft_strlcat(char *dest, const char *src, size_t size);

#endif
