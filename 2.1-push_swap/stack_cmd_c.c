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

void	ft_ss(td_list **stack_a, td_list **stack_b)
{
	ft_stack_swap(stack_a);
	ft_stack_swap(stack_b);
	ft_printf("ss\n");
}

void	ft_rr(td_list **stack_a, td_list **stack_b)
{
	ft_stack_rotate(stack_a);
	ft_stack_rotate(stack_b);
	ft_printf("rr\n");
}

void	ft_rrr(td_list **stack_a, td_list **stack_b)
{
	ft_stack_reverse_rotate(stack_a);
	ft_stack_reverse_rotate(stack_b);
	ft_printf("rrr\n");
}