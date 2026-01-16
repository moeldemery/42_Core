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

#include "push_swap.h"

int	ft_process_arg(char *arg, td_list **stack)
{
	t_element	*element;
	int			num;

	if (ft_is_str_digit(arg) == 0)
		return (0);
	num = ft_atoi(arg);
	element = ft_init_element(num);
	ft_lstd_add_back(stack, ft_lstd_new(element));
	return (1);
}

int	ft_proccess_arg_split(char *arg, td_list **stack)
{
	t_element	*element;
	int			num;
	char		**args_split;
	char		**args_ptr;

	args_split = ft_split(arg, ' ');
	if (!args_split)
		return (ft_printf("Error\n") != 0);
	args_ptr = args_split;
	while (*args_split)
	{
		if (ft_is_str_digit(*args_split) == 0)
		{
			free(args_ptr);
			return (ft_printf("Error\n") != 0);
		}
		num = ft_atoi(*args_split);
		element = ft_init_element(num);
		ft_lstd_add_back(stack, ft_lstd_new(element));
		args_split++;
	}
	free(args_ptr);
	return (1);
}
