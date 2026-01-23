/* ************************************************************************** */
/*                                                                            */
/*                                                        :::      ::::::::   */
/*   arg_support.c                                      :+:      :+:    :+:   */
/*                                                    +:+ +:+         +:+     */
/*   By: meldemir <meldemir@student.42berlin.d      +#+  +:+       +#+        */
/*                                                +#+#+#+#+#+   +#+           */
/*   Created: 2026/01/16 22:20:31 by meldemir          #+#    #+#             */
/*   Updated: 2026/01/16 22:20:32 by meldemir         ###   ########.fr       */
/*                                                                            */
/* ************************************************************************** */

#include "arg_support.h"

int	ft_check_dup(t_d_list *stack, int num)
{
	while (stack)
	{
		if (((t_element *)stack->content)->value == num)
			return (1);
		stack = stack->next;
	}
	return (0);
}

long	ft_atol(const char *str)
{
	long	res;
	int		sign;

	res = 0;
	sign = 1;
	while (*str == ' ' || (*str >= 9 && *str <= 13))
		str++;
	if (*str == '-' || *str == '+')
	{
		if (*str == '-')
			sign = -1;
		str++;
	}
	while (*str >= '0' && *str <= '9')
	{
		res = res * 10 + (*str - '0');
		str++;
	}
	return (res * sign);
}

int	ft_process_arg(char *arg, t_d_list **stack)
{
	t_element	*element;
	long		num;

	if (arg[0] == '\0' || ft_is_str_digit(arg) == 0)
		return (0);
	num = ft_atol(arg);
	if (num > 2147483647 || num < -2147483648)
		return (0);
	if (ft_check_dup(*stack, (int)num))
		return (0);
	element = ft_init_element((int)num);
	ft_lstd_add_back(stack, ft_lstd_new(element));
	return (1);
}

static void	ft_free_split(char **str_array)
{
	int	i;

	if (!str_array)
		return ;
	i = 0;
	while (str_array[i])
	{
		free(str_array[i]);
		i++;
	}
	free(str_array);
}

int	ft_proccess_arg_split(char *arg, t_d_list **stack)
{
	int		i;
	char	**args_split;

	args_split = ft_split(arg, ' ');
	if (!args_split || !args_split[0])
	{
		if (args_split)
			free(args_split);
		return (0);
	}
	i = 0;
	while (args_split[i])
	{
		if (!ft_process_arg(args_split[i], stack))
		{
			ft_free_split(args_split);
			return (0);
		}
		i++;
	}
	ft_free_split(args_split);
	return (1);
}
