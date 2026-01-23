/* ************************************************************************** */
/*                                                                            */
/*                                                        :::      ::::::::   */
/*   stack_cmd_c.c                                      :+:      :+:    :+:   */
/*                                                    +:+ +:+         +:+     */
/*   By: meldemir <meldemir@student.42berlin.d      +#+  +:+       +#+        */
/*                                                +#+#+#+#+#+   +#+           */
/*   Created: 2026/01/10 23:16:13 by meldemir          #+#    #+#             */
/*   Updated: 2026/01/10 23:16:14 by meldemir         ###   ########.fr       */
/*                                                                            */
/* ************************************************************************** */

#include "push_swap.h"

void	ft_ss(t_d_list **stack_a, t_d_list **stack_b, int is_printable)
{
	ft_stack_swap(stack_a);
	ft_stack_swap(stack_b);
	if (is_printable)
		ft_printf("ss\n");
}

void	ft_rr(t_d_list **stack_a, t_d_list **stack_b, int is_printable)
{
	ft_stack_rotate(stack_a);
	ft_stack_rotate(stack_b);
	if (is_printable)
		ft_printf("rr\n");
}

void	ft_rrr(t_d_list **stack_a, t_d_list **stack_b, int is_printable)
{
	ft_stack_reverse_rotate(stack_a);
	ft_stack_reverse_rotate(stack_b);
	if (is_printable)
		ft_printf("rrr\n");
}
