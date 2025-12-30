/* ************************************************************************** */
/*                                                                            */
/*                                                        :::      ::::::::   */
/*   ftprintf.h                                         :+:      :+:    :+:   */
/*                                                    +:+ +:+         +:+     */
/*   By: meldemir <meldemir@student.42berlin.d      +#+  +:+       +#+        */
/*                                                +#+#+#+#+#+   +#+           */
/*   Created: 2025/12/01 13:40:07 by meldemir          #+#    #+#             */
/*   Updated: 2025/12/01 13:40:09 by meldemir         ###   ########.fr       */
/*                                                                            */
/* ************************************************************************** */
#ifndef FT_PRINTF_BONUS_H
# define FT_PRINTF_BONUS_H

# include <stdarg.h>
# include <unistd.h>
# include <stdlib.h>
# include "libft/libft.h"
# define DEC	"0123456789" 
# define HEXS	"0123456789abcdef"
# define HEX	"0123456789ABCDEF"

typedef struct s_flags
{
	int	plus;
	int	space;
	int	minus;
	int	hash;
	int	zero;
	int	width;
	int	padding;
}	t_flags;

int		ft_printf(const char *str, ...);

size_t	ft_putnbr_base(long long nbr, char *base);
size_t	ft_putnbr_base_unsigned(unsigned long long nbr, char *base);
int		ft_num_len_base(unsigned long long n, int base_len);

size_t	ft_check_format(const char **str, va_list *args1);
int		ft_print_clasifier(const char *str, va_list *args, t_flags f);
int		ft_print_clasifier_bonus(const char **str, va_list *args2);
void	ft_flag_parser(const char **str, t_flags *f);

int		ft_print_char_bonus(int c, t_flags f);
int		ft_print_int_bonus(int n, t_flags f);
int		ft_print_u_int_bonus(unsigned int n, t_flags f);
int		ft_print_add_b(unsigned long addr, t_flags f);
int		ft_print_hex_bonus(unsigned int n, char type, t_flags f);
int		ft_print_str_bonus(char *s, t_flags f);
int		ft_print_percent_bonus(t_flags f);

#endif