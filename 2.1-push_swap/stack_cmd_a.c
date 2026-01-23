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

void	ft_sa(t_d_list **stack_a, int is_printable)
{
	ft_stack_swap(stack_a);
	if (is_printable)
		ft_printf("sa\n");
}

void	ft_pa(t_d_list **stack_a, t_d_list **stack_b, int is_printable)
{
	ft_stack_push(stack_b, stack_a);
	if (is_printable)
		ft_printf("pa\n");
}

void	ft_ra(t_d_list **stack_a, int is_printable)
{
	ft_stack_rotate(stack_a);
	if (is_printable)
		ft_printf("ra\n");
}

void	ft_rra(t_d_list **stack_a, int is_printable)
{
	ft_stack_reverse_rotate(stack_a);
	if (is_printable)
		ft_printf("rra\n");
}
