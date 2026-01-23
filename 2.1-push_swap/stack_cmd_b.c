/* ************************************************************************** */
/*                                                                            */
/*                                                        :::      ::::::::   */
/*   stack_cmd_b.c                                      :+:      :+:    :+:   */
/*                                                    +:+ +:+         +:+     */
/*   By: meldemir <meldemir@student.42berlin.d      +#+  +:+       +#+        */
/*                                                +#+#+#+#+#+   +#+           */
/*   Created: 2026/01/10 23:16:07 by meldemir          #+#    #+#             */
/*   Updated: 2026/01/10 23:16:09 by meldemir         ###   ########.fr       */
/*                                                                            */
/* ************************************************************************** */

#include "push_swap.h"

void	ft_sb(t_d_list **stack_b, int is_printable)
{
	ft_stack_swap(stack_b);
	if (is_printable)
		ft_printf("sb\n");
}

void	ft_pb(t_d_list **stack_a, t_d_list **stack_b, int is_printable)
{
	ft_stack_push(stack_a, stack_b);
	if (is_printable)
		ft_printf("pb\n");
}

void	ft_rb(t_d_list **stack_b, int is_printable)
{
	ft_stack_rotate(stack_b);
	if (is_printable)
		ft_printf("rb\n");
}

void	ft_rrb(t_d_list **stack_b, int is_printable)
{
	ft_stack_reverse_rotate(stack_b);
	if (is_printable)
		ft_printf("rrb\n");
}
