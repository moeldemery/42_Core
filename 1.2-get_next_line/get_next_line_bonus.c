/* ************************************************************************** */
/*                                                                            */
/*                                                        :::      ::::::::   */
/*   get_next_line_bonus.c                              :+:      :+:    :+:   */
/*                                                    +:+ +:+         +:+     */
/*   By: meldemir <meldemir@student.42berlin.d      +#+  +:+       +#+        */
/*                                                +#+#+#+#+#+   +#+           */
/*   Created: 2025/12/17 15:57:28 by meldemir          #+#    #+#             */
/*   Updated: 2025/12/17 15:57:39 by meldemir         ###   ########.fr       */
/*                                                                            */
/* ************************************************************************** */

#include "get_next_line_bonus.h"

char	*_create_empty_buffer(char **buffer)
{
	if (*buffer == NULL)
	{
		*buffer = (char *)malloc(sizeof(char) * (1));
		if (*buffer == NULL)
			return (NULL);
		(*buffer)[0] = '\0';
	}
	return (*buffer);
}

int	_fill_buffer(char **buffer, int fd)
{
	int		bytes_read;
	char	read_buffer [BUFFER_SIZE + 1];
	char	*temp_join;

	bytes_read = read(fd, read_buffer, BUFFER_SIZE);
	if (bytes_read == -1)
		return (bytes_read);
	read_buffer[bytes_read] = '\0';
	temp_join = malloc(ft_strlen(*buffer) + bytes_read + 1);
	if (!temp_join) 
		return (-1);
	ft_strlcpy(temp_join, *buffer, ft_strlen(*buffer) + 1);
	ft_strlcat(temp_join, read_buffer, ft_strlen(*buffer) + bytes_read + 1);
	free(*buffer);
	*buffer = temp_join;
	return (bytes_read);
}

char	*_get_line(char **buf, int newline_index)
{
	char	*line;
	char	*temp;
	ssize_t	buf_len;

	buf_len = ft_strlen(*buf);
	line = ft_substr (*buf, 0, newline_index + 1);
	if (!line)
		return (NULL);
	temp = ft_substr (*buf, newline_index + 1, buf_len - newline_index - 1);
	if (!temp) 
	{
		free(line); 
		return (NULL);
	}
	free(*buf);
	*buf = temp;
	return (line);
}

char	*_check_buffer(char **buffer)
{
	int		newline_index;
	char	*line;

	if (*buffer == NULL || (*buffer)[0] == '\0')
	{
		if (*buffer) 
			free(*buffer);
		*buffer = NULL;
		return (NULL);
	}
	newline_index = ft_strchr_index(*buffer, '\n', ft_strlen(*buffer));
	if (newline_index >= 0)
	{
		line = _get_line(buffer, newline_index);
		return (line);
	}
	else
	{
		line = ft_substr(*buffer, 0, ft_strlen(*buffer));
		free(*buffer);
		*buffer = NULL; 
		return (line);
	}
}

char	*get_next_line(int fd)
{
	static char	*buffer[FD_MAX_NUMBER];
	int			bytes_read;
	ssize_t		line_index;

	if (fd < 0 || fd >= FD_MAX_NUMBER || BUFFER_SIZE <= 0)
		return (NULL);
	if (!_create_empty_buffer(&buffer[fd])) 
		return (NULL);
	bytes_read = 1;
	line_index = ft_strchr_index(buffer[fd], '\n', ft_strlen(buffer[fd]));
	while (line_index < 0 && bytes_read > 0)
	{
		bytes_read = _fill_buffer(&buffer[fd], fd);
		if (bytes_read == -1) 
		{
			if (buffer[fd])
				free(buffer[fd]);
			buffer[fd] = NULL;
			return (NULL);
		}
		line_index = ft_strchr_index(buffer[fd], '\n', ft_strlen(buffer[fd]));
	}
	return (_check_buffer(&buffer[fd]));
}
