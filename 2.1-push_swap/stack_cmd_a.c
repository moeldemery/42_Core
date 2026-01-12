/* ************************************************************************** */
/*                                                                            */
/*                                                        :::      ::::::::   */
/*   stack_cmd_a.c                                      :+:      :+:    :+:   */
/*                                                    +:+ +:+         +:+     */
/*   By: meldemir <meldemir@student.42berlin.d      +#+  +:+       +#+        */
/*                                                +#+#+#+#+#+   +#+           */
/*   Created: 2026/01/10 23:16:02 by meldemir          #+#    #+#             */
/*   Updated: 2026/01/10 23:16:03 by meldemir         ###   ########.fr       */
/*                                                                            */
/* ************************************************************************** */
#include "push_swap.h"

void	ft_sa(t_list **stack_a)
{
	ft_stack_swap(stack_a);
	ft_printf("sa\n");
}

void	ft_pa(t_list **stack_a, t_list **stack_b)
{
	ft_stack_push(stack_b, stack_a);
	ft_printf("pa\n");
}

void	ft_ra(t_list **stack_a)
{
	ft_stack_rotate(stack_a);
	ft_printf("ra\n");
}

void	ft_rra(t_list **stack_a)
{
	ft_stack_reverse_rotate(stack_a);
	ft_printf("rra\n");
}
